import tempfile
import unittest
from pathlib import Path

from bot.services.knowledge import search_knowledge


class KnowledgeSearchTests(unittest.TestCase):
    def test_searches_local_public_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "05-common-errors.md").write_text(
                "# 常见报错\n关键词：502 503 上游 超时\n\n- 502 通常表示上游链路异常。\n",
                encoding="utf-8",
            )
            (root / "07-payment.md").write_text(
                "# 充值说明\n关键词：充值 USDT 首充\n\n- 充值使用 USDT-TRC20。\n",
                encoding="utf-8",
            )

            hits = search_knowledge("502 bad gateway 怎么办", root)

            self.assertGreaterEqual(len(hits), 1)
            self.assertEqual(hits[0].name, "05-common-errors.md")
            self.assertIn("上游", hits[0].snippet)


if __name__ == "__main__":
    unittest.main()

