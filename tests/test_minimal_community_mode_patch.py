import unittest

from scripts.patch_minimal_community_mode import patch_bot_text, patch_payout_text


class MinimalCommunityModePatchTests(unittest.TestCase):
    def test_bot_patch_adds_allowlist_and_base_only_copy(self):
        source = """
function myBenefits(uid, name) { return 'old'; }
function weeklyBenefitInfo() { return 'old'; }
function balanceBenefitGuide(uid, name) { return 'old'; }
function benefitRules() { return 'old'; }
function promoReply(raw, uid, name) { return null; }
async function handleCommand(text, msg = {}) {
  const raw = String(text || '').trim();
  if (!raw) return null;
}
async function processIncomingMessage(m, options = {}) {
  const raw = m.text || '';
  if (ownerMentioned(raw, m)) {
  }
}
"""
        patched = patch_bot_text(source)
        self.assertIn("minimal-community-mode-20260712", patched)
        self.assertIn("!isMinimalCommunityCommand(raw)", patched)
        self.assertIn("每周一次，每人 +2", patched)
        self.assertIn("签到、积分、周榜、排名奖励、抽奖券及全部游戏玩法", patched)
        self.assertIn("reason: 'minimal_community_mode'", patched)
        self.assertIn("const minimalReply = await handleCommand(raw, m)", patched)
        self.assertIn("minimalCommunityMode: true", patched)

    def test_payout_patch_disables_rank_plan_and_restricts_mark_paid(self):
        source = """
const state = readJson(statePath);
const paid = payoutState(state).paid;
if (cmd === 'plan') {}
else if (cmd === 'mark-paid') {
  const plan = readJson(path.resolve(root, planPath));
  const expected = `MARK_WEEKLY_PAYOUT_${plan.weekKey}`;
}
"""
        patched = patch_payout_text(source)
        self.assertIn("minimal-base-welfare-only-20260712", patched)
        self.assertIn("cmd === 'plan'", patched)
        self.assertIn("endsWith('-base-2yuan')", patched)
        self.assertIn("Number(item.amount) !== 2", patched)

    def test_patch_is_idempotent(self):
        source = """
function myBenefits(uid, name) { return 'old'; }
function weeklyBenefitInfo() { return 'old'; }
function balanceBenefitGuide(uid, name) { return 'old'; }
function benefitRules() { return 'old'; }
function promoReply(raw, uid, name) { return null; }
async function handleCommand(text, msg = {}) {
  const raw = String(text || '').trim();
  if (!raw) return null;
}
async function processIncomingMessage(m, options = {}) {
  const raw = m.text || '';
  if (ownerMentioned(raw, m)) {
  }
}
"""
        once = patch_bot_text(source)
        self.assertEqual(once, patch_bot_text(once))


if __name__ == "__main__":
    unittest.main()
