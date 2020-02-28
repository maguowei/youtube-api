# youtube-api

YouTube API on AWS Lambda

`/api/?url={URL}`

Example
- `/api/?url=https://www.youtube.com/watch?v=BR_QeAv09L8`
- `/api/?url=https://www.youtube.com/playlist?list=PLbWPytS1GWJJnhWo338YPZDNTTeCVIC37`

## dev

```bash
pipenv install
```

## Deploy

```bash
chalice deploy
```

- [aws/chalice](https://github.com/aws/chalice)
