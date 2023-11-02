# Configuration Reference

The **`nmk-badges`** plugin handles the configuration items listed in this page.

All of them are initiliazed with convenient default values, so that you don't need to setup them for a default working behavior. You can anyway override them in your projet if you need to fine tune the plugin behavior. [Some items](extend.md) are specifically designed to be extended by **`nmk`** projects and plugins.

## Files

(badgesTarget)=
### **`badgesTarget`** -- target README.md file

| Type | Default value |
|-     |-
| str  | ${PROJECTDIR}/README.md

Target **README.md** file where generated badges will be inserted

(badgesStamp)=
### **`badgesStamp`** -- badges stamp file

| Type | Default value |
|-     |-
| str  | **[${outputDir}](https://nmk-base.readthedocs.io/en/stable/config.html#outputdir-output-base-directory)**/.badges

Stamp file to track the last time the **{ref}`${badgesTarget}<badgesTarget>`** file was updated with generated badges.

## Patterns

(badgesBeginPattern)=
### **`badgesBeginPattern`** -- begin pattern

| Type | Default value |
|-     |-
| str  | `<!-- NMK-BADGES-BEGIN -->`

Begin pattern for the **{ref}`${badgesTarget}<badgesTarget>`** file area to be updated with generated badges.

(badgesEndPattern)=
### **`badgesEndPattern`** -- end pattern

| Type | Default value |
|-     |-
| str  | `<!-- NMK-BADGES-END -->`

End pattern for the **{ref}`${badgesTarget}<badgesTarget>`** file area to be updated with generated badges.

## Badges

(badgesConfig)=
### **`badges`** -- badges definition

| Type | Default value |
|-     |-
| List[Dict[str,str]]  | {}

This configuration is a list of badges to be inserted in the **{ref}`${badgesTarget}<badgesTarget>`** file.

Each item in the list is a dictionnary, expected to have the following keys:

* **`alt`**: alternative descriptive text for the badge
* **`img`**: URL to badge generated image
* **`url`**: target URL for badge link
* **`if`**: when set, the badge will be generated only if the provided condition is met
* **`unless`**: when set, the badge will be generated unless the provided condition is met

Note that badges conditions are handled the same way than task ones.
