import shutil
from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestProtoPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    @property
    def readme(self) -> Path:
        return self.test_folder / "README.md"

    def prepare_badge_project(self, readme: str = None) -> Path:
        # Build a sample project with proto files
        if readme is not None:
            shutil.copyfile(self.template(f"{readme}.md"), self.readme)
        return self.prepare_project("ref_badges.yml")

    def compare_readme(self, readme: str, is_ok: bool = True):
        with self.template(f"{readme}.md").open() as a, self.readme.open() as b:
            if is_ok:
                assert a.readlines() == b.readlines()
            else:
                assert a.readlines() != b.readlines()

    def test_version(self):
        self.nmk(self.prepare_badge_project(), extra_args=["version"])

    def test_missing_begin_pattern(self):
        self.nmk(self.prepare_badge_project("no_begin"), extra_args=["badges"])
        self.check_logs("WARNING ❗ - Invalid or missing pattern in README.md file")
        self.compare_readme("no_begin")

    def test_missing_end_pattern(self):
        self.nmk(self.prepare_badge_project("no_end"), extra_args=["badges"])
        self.check_logs("WARNING ❗ - Invalid or missing pattern in README.md file")
        self.compare_readme("no_end")

    def test_ok(self):
        self.nmk(self.prepare_badge_project("ok"), extra_args=["badges"])
        self.compare_readme("no_end", False)
        with self.readme.open() as r:
            assert "[![Some text](http://foo.org/bar.png)](http://path.to/foo)" in r.read()
