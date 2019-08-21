#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the response#
curl -d "$1" "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST https://flaviocopes.com/
