![](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F-at%20Technologiestiftung%20Berlin-blue)

# Download Fis-Broker Data

_This is a script to fetch data from the Fis-Broker of Berlin and save it as a GeoJSON._


## Example usage

get_data_from_wfs.py -l s_wfs_baumbestand -v

## Usage

usage: get_data_from_wfs.py [-h] [-l LAYER] [-v] [-fp FILE_PATH] [-fn FILE_NAME] [-url BASE_URL] [-of OUTPUT_FORMAT]

options:

  -h, --help            show this help message and exit

  -l LAYER, --layer LAYER

                        The name of the layer. Use '-' instead of ':'

  -v, --verbose         Show more info

  -fp FILE_PATH, --file_path FILE_PATH

                        Base path to store files with trailing slash

  -fn FILE_NAME, --file_name FILE_NAME

                        Optional, by default it will be named like the layer.

  -url BASE_URL, --base_url BASE_URL

                        Optional, by default FIS broker URL.

  -of OUTPUT_FORMAT, --output_format OUTPUT_FORMAT

                        Optional, by default 'text/xml; subtype=gml/3.2.1'


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Lisa-Stubert"><img src="https://avatars.githubusercontent.com/u/61182572?v=4?s=64" width="64px;" alt=""/><br /><sub><b>Lisa-Stubert</b></sub></a><br /><a href="#data-Lisa-Stubert" title="Data">🔣</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-tree-data/commits?author=Lisa-Stubert" title="Code">💻</a> <a href="https://github.com/technologiestiftung/giessdenkiez-de-tree-data/commits?author=Lisa-Stubert" title="Documentation">📖</a></td>
 <td align="center"><a href="https://www.technologiestiftung-berlin.de/de/citylab/"><img src="https://avatars.githubusercontent.com/u/91873654?v=4?s=64" width="64px;" alt=""/><br /><sub><b>juan-carlos-tsb</b></sub></a><br /><a href="https://github.com/technologiestiftung/qtrees-vectortiles-generator/commits?author=juan-carlos-tsb" title="Code">💻</a> <a href="#design-juan-carlos-tsb" title="Design">🎨</a> <a href="https://github.com/technologiestiftung/qtrees-vectortiles-generator/pulls?q=is%3Apr+reviewed-by%3Ajuan-carlos-tsb" title="Reviewed Pull Requests">👀</a> <a href="#ideas-juan-carlos-tsb" title="Ideas, Planning, Code">🤔</a></td>   
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
