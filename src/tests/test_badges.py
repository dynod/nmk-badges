from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestProtoPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def prepare_proto_project(self, other_plugin: str = None) -> Path:
        # Build a sample project with proto files
        return self.prepare_project(f"ref_badges{('_'+other_plugin) if other_plugin is not None else ''}.yml")

    def escape(self, to_escape: Path) -> str:
        # Escape backslashes (for Windows paths in json print)
        return str(to_escape).replace("\\", "\\\\")

    def test_version(self):
        self.nmk(self.prepare_proto_project(), extra_args=["version"])
