#!/usr/bin/env python3
import argparse
import hashlib
from pathlib import Path


EXPECTED_BOT_SHA256 = "7f0ad3d8680f46d3950e5831f01a5fad59da9a1e536e9b823f9580f2185e6efa"
EXPECTED_PAYOUT_SHA256 = "8b268f4ddcc0e07324075eb6831d1b336ba5c7d059a5866c490822d900678293"
PATCH_MARKER = "minimal-community-mode-20260712"


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    start_index = text.find(start)
    if start_index < 0:
        raise ValueError(f"missing start anchor: {start}")
    end_index = text.find(end, start_index)
    if end_index < 0:
        raise ValueError(f"missing end anchor: {end}")
    return text[:start_index] + replacement.rstrip() + "\n" + text[end_index:]


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"expected one anchor, found {count}: {old[:80]}")
    return text.replace(old, new, 1)


def patch_bot_text(text: str) -> str:
    if PATCH_MARKER in text:
        return text

    my_benefits = r'''function myBenefits(uid, name) {
  const user = getUser(uid, name);
  const binding = ensureBinding(user);
  const bindingReady = binding.status === 'bound' && binding.tier === 'free_community' && !binding.rewardBlocked;
  return cyberCard('社区绑定 · 我的状态', [
    bar('玩家', user.name),
    bar('绑定状态', binding.status || 'unbound'),
    bar('基础周福利', bindingReady ? '已满足绑定条件' : '暂不满足绑定条件'),
    '结算条件｜发放时中转站真实余额严格大于 10',
    '福利额度｜每周一次，每人 +2 体验余额',
    '说明｜不再设置签到、积分、周榜、排名奖或其他游戏奖励',
  ], '最终名单以管理员按真实绑定和实时余额核对为准');
}'''
    weekly_info = r'''function weeklyBenefitInfo() {
  return cyberCard('周基础福利 · 社区绑定账号', [
    '参与条件｜已完成社区绑定，且绑定状态有效',
    '余额条件｜发放时中转站真实余额严格大于 10',
    '福利额度｜每周一次，每人 +2 体验余额',
    '发放方式｜管理员核对名单、备份并记录余额流水后发放',
    '已取消｜签到、积分、周榜、排名奖励、抽奖券及全部游戏玩法',
    '提醒｜福利不计入真实充值，不支持提现、转让或折现',
  ], '机器人只保留社区绑定与周基础福利');
}'''
    balance_guide = r'''function balanceBenefitGuide(uid, name) {
  const user = getUser(uid, name);
  const binding = ensureBinding(user);
  const bindingReady = binding.status === 'bound' && binding.tier === 'free_community' && !binding.rewardBlocked;
  return cyberCard('周基础福利 · 获取方式', [
    bar('玩家', user.name),
    bar('绑定状态', binding.status || 'unbound'),
    bar('绑定资格', bindingReady ? '已满足' : '需先完成社区绑定'),
    '入口｜皓悦API → 兑换 → 社区绑定，填写社区邮箱和绑定码',
    '余额条件｜发放时中转站真实余额严格大于 10',
    '福利额度｜每周一次，每人 +2 体验余额',
    '说明｜不再依据签到、游戏积分、周排名或抽奖券发放余额',
  ], '管理员按真实绑定和实时余额人工核对');
}'''
    benefit_rules = r'''function benefitRules() {
  return cyberCard('周基础福利 · 规则', [
    '1｜必须完成社区绑定并保持绑定有效',
    '2｜结算时中转站真实余额必须严格大于 10',
    '3｜符合条件者每周发放 +2 体验余额',
    '4｜同一周同一账号只发放一次，并记录余额流水',
    '5｜签到、积分、周榜、排名奖励、抽奖券和全部游戏玩法均已取消',
    '6｜福利不计入真实充值，不支持提现、转让或折现',
  ], '最终名单以管理员核对结果为准');
}'''

    text = replace_between(text, "function myBenefits(uid, name) {", "function weeklyBenefitInfo() {", my_benefits)
    text = replace_between(text, "function weeklyBenefitInfo() {", "function balanceBenefitGuide(uid, name) {", weekly_info)
    text = replace_between(text, "function balanceBenefitGuide(uid, name) {", "function benefitRules() {", balance_guide)
    text = replace_between(text, "function benefitRules() {", "function promoReply(", benefit_rules)

    minimal_gate = r'''// minimal-community-mode-20260712: only binding and the +2 base weekly welfare remain.
function isMinimalCommunityCommand(raw) {
  const text = String(raw || '')
    .replace(/@[^\s]+/g, ' ')
    .replaceAll(config.botName || '皓悦小助手', ' ')
    .trim();
  return /^(?:\/|！|!|#)?\s*(?:绑定状态|绑定|我的绑定|我的权益|周福利|福利规则|余额福利)(?:\s|[？?！!。]|$)/.test(text);
}

'''
    text = replace_once(text, "async function handleCommand(text, msg = {}) {", minimal_gate + "async function handleCommand(text, msg = {}) {")
    text = replace_once(
        text,
        "  const raw = String(text || '').trim();\n  if (!raw) return null;",
        "  const raw = String(text || '').trim();\n  if (!raw || !isMinimalCommunityCommand(raw)) return null;",
    )
    text = replace_once(
        text,
        "  const raw = m.text || '';\n  if (ownerMentioned(raw, m)) {",
        "  const raw = m.text || '';\n"
        "  if (!isMinimalCommunityCommand(raw)) {\n"
        "    logEvent('ignore', { roomId: currentRoomId, reason: 'minimal_community_mode', messageId: m.id, from, text: raw });\n"
        "    return;\n"
        "  }\n"
        "  {\n"
        "    const minimalReply = await handleCommand(raw, m);\n"
        "    if (minimalReply) {\n"
        "      await sendRoomMessage(minimalReply, { toRoomId: currentRoomId, triggerMessageId: m.id, triggerText: raw, triggerFrom: from, minimalCommunityMode: true, replay });\n"
        "    } else {\n"
        "      logEvent('no_reply', { roomId: currentRoomId, reason: 'minimal_community_mode', messageId: m.id, from, text: raw, replay });\n"
        "    }\n"
        "    return;\n"
        "  }\n"
        "  if (ownerMentioned(raw, m)) {",
    )
    return text


def patch_payout_text(text: str) -> str:
    marker = "minimal-base-welfare-only-20260712"
    if marker in text:
        return text
    text = replace_once(
        text,
        "const state = readJson(statePath);\nconst paid = payoutState(state).paid;",
        "const state = readJson(statePath);\nconst paid = payoutState(state).paid;\n\n"
        "// minimal-base-welfare-only-20260712: variable game/rank plans are permanently disabled.\n"
        "if (cmd === 'plan') {\n"
        "  console.error('Game and rank payout plans are disabled. Generate only an externally verified base plan: effective community binding, live balance > 10, amount exactly 2.');\n"
        "  process.exit(3);\n"
        "}",
    )
    text = replace_once(
        text,
        "  const plan = readJson(path.resolve(root, planPath));\n  const expected = `MARK_WEEKLY_PAYOUT_${plan.weekKey}`;",
        "  const plan = readJson(path.resolve(root, planPath));\n"
        "  const items = Array.isArray(plan.items) ? plan.items : [];\n"
        "  if (!String(plan.weekKey || '').endsWith('-base-2yuan') || !items.length || items.some(item => Number(item.amount) !== 2)) {\n"
        "    console.error('Only a non-empty *-base-2yuan plan with amount exactly 2 per user may be marked paid.');\n"
        "    process.exit(3);\n"
        "  }\n"
        "  const expected = `MARK_WEEKLY_PAYOUT_${plan.weekKey}`;",
    )
    return text


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bot", required=True, type=Path)
    parser.add_argument("--payout", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    bot_raw = args.bot.read_bytes()
    payout_raw = args.payout.read_bytes()
    bot_text = bot_raw.decode("utf-8").replace("\r\n", "\n")
    payout_text = payout_raw.decode("utf-8").replace("\r\n", "\n")
    if PATCH_MARKER not in bot_text and sha256_bytes(bot_raw) != EXPECTED_BOT_SHA256:
        raise SystemExit("bot.mjs baseline hash mismatch")
    if "minimal-base-welfare-only-20260712" not in payout_text and sha256_bytes(payout_raw) != EXPECTED_PAYOUT_SHA256:
        raise SystemExit("weekly-payout-admin.mjs baseline hash mismatch")

    patched_bot = patch_bot_text(bot_text)
    patched_payout = patch_payout_text(payout_text)
    result = {
        "bot_before": sha256_bytes(bot_raw),
        "bot_after": sha256(patched_bot),
        "payout_before": sha256_bytes(payout_raw),
        "payout_after": sha256(patched_payout),
        "changed": patched_bot != bot_text or patched_payout != payout_text,
    }
    if args.apply:
        args.bot.write_text(patched_bot, encoding="utf-8")
        args.payout.write_text(patched_payout, encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
