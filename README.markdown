xkcd password
=============

An implementation of:
http://xkcd.com/936/

Requisites
----------
- Any old python

- a dictionary (in /usr/share/dict/words by default)

Usage
-----
help!
    $ ./xkcd-password.py --help

Run with default of 10 passwords, each with 4 words:
    $ ./xkcd-password.py

    emulsion odyssey antagonized exasperated
    drip transcribed industrializes hauling
    enslavement conversion outputting traces
    woozy constraining crocus digestions
    ignored alkalis juggles efficaciously
    tourneys temperamentally ornateness vectoring
    amass gruelled billet stolid
    marriage perjurers corporals decencies
    targets hallucinogenic runaways bashed
    ricochets sodas mangle pedagoguing

More memorable - short words, 100 passwords, grid mode:
(ie. take your pick from the grid)

    $ ./xkcd-password.py --min 3 --max 6 --grid -n 100

    routs  side   repeal mentor
    been   milks  how    faker 
    cored  direst foe    auto  
    edify  shift  aims   umped 
    midge  orb    bell   limned
    ...
    etc
