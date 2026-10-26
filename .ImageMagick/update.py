#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

URL = "https://github.com/cisco/openh264/archive/refs/tags/v{version}.tar.gz"


def update_source(updater):
    updater.replace_source()
    updater.remove(".github")
    updater.update_config()


def apply_patches(updater):
    updater.apply_patches()


updater = Updater(__file__, "openh264", URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Updated openh264 to {version}"),
    Step("Move version methods to the decoder because we don't build the encoder",
        apply_patches,
        "Move version methods to the decoder because we don't build the encoder."),
    updater.clone_dependencies_step(),
])
