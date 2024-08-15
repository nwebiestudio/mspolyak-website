# Web-site of Dr. Polyak M.S., professor of microbiology

## Developmemt

> Site is build with [pelican](https://docs.getpelican.com/en/latest/)

**To run locally:**

```bash
git clone https://github.com/nwebiestudio/mspolyak-website

cd mspolyak-website

poetry install

pelican content

pelican -l -r
```

and go to http://locahost:8000

---

All sources are kept in `content` folder. `theme` folder contains modified
[lovers](https://github.com/chdoig/pelican-bootstrap3-lovers/tree/234de548b4dd5f5779597fd27075723e80b7384f)
theme.
