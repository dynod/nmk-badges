# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-badges!plugin.yml
```

Then you can start adding badges in your top level **README.md** file by:
* adding in your **README.md** file the **`<!-- NMK-BADGES-BEGIN -->`** and **`<!-- NMK-BADGES-END -->`** delimiters where you want to insert the badges
* extending the **{ref}`${badges}<badgesDef>`** config item to add badges
