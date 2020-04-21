import re
import shutil
from pathlib import Path
from typing import List


class QueryLogger:
    def __init__(
        self,
        enabled=True,
        startIndex=0,
        deleteDirectory="sparql.tmp",
        template="sparql.tmp/{qr}{index}{query}.{ext}",
        queryTemplate=None,
        resultTemplate=None,
    ):
        if deleteDirectory is not None:
            shutil.rmtree(deleteDirectory)

        if queryTemplate is None:
            queryTemplate = self._expand(template, "query", "sparql")

        if resultTemplate is None:
            resultTemplate = self._expand(template, "request", "csv")

        self._queryTemplate = queryTemplate
        self._resultTemplate = resultTemplate
        self._enabled = enabled
        self._index = startIndex

    def _expand(self, template, qrWord, ext):
        return (
            template.replace("{qr}", qrWord[:1])
            .replace("{qrWord}", qrWord)
            .replace("{ext}", ext)
        )

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def _format(self, template, query):
        return template.format(query=query, index=self._index)

    def _querify(self, word: str):
        letterOnly = re.sub(r"[^a-zA-z]", " ", word)
        x = re.sub(r" +", ".", letterOnly.strip())
        return x

    def write(self, select: str, where: List[str], fullQuery: str, result):
        if not self._enabled:
            return
        if len(where) > 2:
            where = [where[0], where[-1]]
        query = "_".join(map(self._querify, [select, *where]))
        queryLogFile = Path(self._format(self._queryTemplate, query))
        resultLogFile = Path(self._format(self._resultTemplate, query))
        self._index += 1

        queryLogFile.parent.mkdir(parents=True, exist_ok=True)
        queryLogFile.write_text(fullQuery)
        resultLogFile.write_text("\n".join(",".join(x) for x in result))
