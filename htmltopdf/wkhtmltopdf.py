# -*- coding: utf-8 -*-
import logging
import subprocess
import tempfile

WKHTMLTOPDF = "wkhtmltopdf"


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def wkhtmltopdf(pdf_path, html_path):
    try:
        logger.debug("converting %s to %s", html_path, pdf_path)
        subprocess.call([WKHTMLTOPDF, html_path, pdf_path])
    except OSError:
        logger.error("Could not use %s", WKHTMLTOPDF)


def htmltopdf(pdf_path, html_path=None, html_content=None):
    if html_content:
        with tempfile.NamedTemporaryFile(suffix='.html') as fp:
            logger.debug("writing temp file %s", fp.name)
            fp.write(html_content)
            fp.flush()
            wkhtmltopdf(pdf_path, fp.name)
    else:
        wkhtmltopdf(pdf_path, html_path)
