# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-badges`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

(badgesDef)=
## Badges definition

**`nmk`** plugins can contribute to the **{ref}`badges<badgesConfig>`** item to define some badges to be inserted in the project main **README.md** file.

Example:
```yaml
badges:
    - alt: some sample badge
      img: https://img.shields.io/badge/any_text-you_like-blue
      url: https://github.com/dynod/nmk-badges
```
