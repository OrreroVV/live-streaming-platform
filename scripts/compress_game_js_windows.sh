#! /bin/bash

JS_PATH=D:/Code/Python/liveStreamingPlatform/liveStreamingPlatform/streamingPlatform/static/flv/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/

find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js


echo yes | python manage.py collectstatic