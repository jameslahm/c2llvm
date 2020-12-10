#!/bin/bash

strip(){
    i=0
    for f; do
        sed -r '
            /<\/?resources>/ d
            s/>/>'$((i++))'/
        ' "$f"
    done
}

strip "$@" | sort -u -k1,1 -t'>' | sed '
    1 s|^|<resources>\n|
    s/>[0-9]/>/
    $ a </resources>
'