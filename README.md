![](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F-at%20Technologiestiftung%20Berlin-blue)

# Download Fis-Broker Data

_This is a script to fetch data from the Fis-Broker of Berlin and save it as a GeoJSON._


## Inputs

- New tree data in GML or GeoJSON format
- config.yaml that configurates paths, tablesnames, overwritting, mapping of column names and columns to update

```yml
database:
  parameter-path: .env
  data-table-name: trees
  replace-table: True

new-data-paths:
  - tree_data/data_files/s_wfs_baumbestand.gml
  - tree_data/data_files/s_wfs_baumbestand_an.gml

data-schema:
  mapping:
    art_bot: artbot
    art_dtsch: artdtsch
    gattung_deutsch: gattungdeutsch
    gml_id: gmlid
  merge-on:
    - gmlid
  update:
    - standalter
    - baumhoehe
    - kronedurch
    - stammumfg
    - gmlid
    - lat
    - lng
    - standortnr
    - kennzeich
    - artdtsch
    - artbot
    - gattungdeutsch
    - gattung
    - pflanzjahr
```

- .env that contains database credentials

```yml
PG_SERVER=
PG_PORT=
PG_USER=
PG_PASS=
PG_DB=
```

## Example Usage

To save newest tree data from the FIS-Broker locally run

```bash
python tree_data/get_data_from_wfs.py
```

To update database run

```bash
python tree_data/main.py
```

## Updating Caretaker labels

In Gieß den Kiez it is visible which trees are maintained by Berlin's street and green space offices. However, this information is not included in the offical Berlin tree dataset. Instead, Berlin's green space offices provide separate Excel tables containing the trees they water. This information needs to be entered 'manually' into the database table "trees" using SQL commands. The procedure is as follows:

1. Extract only the FIS-Broker-ID'S (gmlids) from the Excel sheet to a csv file
2. Create a new table with this ID's in the database: `CREATE TABLE caretaker_ids(id VARCHAR NOT NULL)`
3. Import ID’s from CSV-Table into the database table
4. Delete old caretaker labels from the trees table: `UPDATE trees SET caretaker = NULL`
5. JOIN new caretaker labels to the trees: `UPDATE trees t SET caretaker = 'Bezirk XY' FROM caretaker_ids c WHERE t.gmlid = c.id`
6. Delete the no longer needed table: `DROP TABLE caretaker_ids`

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Lisa-Stubert"><img src="https://avatars.githubusercontent.com/u/61182572?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lisa-Stubert</b></sub></a><br /><a href="#data-Lisa-Stubert" title="Data">🔣</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-tree-data/commits?author=Lisa-Stubert" title="Code">💻</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-tree-data/commits?author=Lisa-Stubert" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/vogelino"><img src="https://avatars.githubusercontent.com/u/2759340?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lucas Vogel</b></sub></a><br /><a href="https://github.com/technologiestiftung/giessdenkiez-de-tree-data/commits?author=vogelino" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

<table>
  <tr>
    <td>
      <a src="https://citylab-berlin.org/en/start/">
        <br />
        <br />
        <img width="200" src="https://logos.citylab-berlin.org/logo-citylab-berlin.svg" />
      </a>
    </td>
    <td>
      A project by: <a src="https://www.technologiestiftung-berlin.de/en/">
        <br />
        <br />
        <img width="150" src="https://logos.citylab-berlin.org/logo-technologiestiftung-berlin-en.svg" />
      </a>
    </td>
    <td>
      Supported by:
      <br />
      <br />
      <img width="120" src="https://logos.citylab-berlin.org/logo-berlin.svg" />
    </td>
  </tr>
</table>
