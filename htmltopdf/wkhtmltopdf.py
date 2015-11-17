# -*- coding: utf-8 -*-
import logging
import shutil
import subprocess
import tempfile

WKHTMLTOPDF = "wkhtmltopdf"


try:
    wkhtmltopdf_path = shutil.which(WKHTMLTOPDF)
except AttributeError:
    import distutils
    wkhtmltopdf_path = distutils.spawn.find_executable(WKHTMLTOPDF)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def wkhtmltopdf(pdf_path, html_path):
    try:
        logger.debug("converting %s to %s", html_path, pdf_path)
        subprocess.call([wkhtmltopdf_path, html_path, pdf_path])
    except OSError:
        logger.error("Could not use %s", wkhtmltopdf_path)


def htmltopdf(pdf_path, html_path=None, html_content=None):
    if html_content:
        with tempfile.NamedTemporaryFile(suffix='.html') as fp:
            logger.debug("writing temp file %s", fp.name)
            fp.write(html_content)
            fp.flush()
            wkhtmltopdf(pdf_path, fp.name)
    else:
        wkhtmltopdf(pdf_path, html_path)
