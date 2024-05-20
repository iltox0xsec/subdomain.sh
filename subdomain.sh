#!/bin/bash

# Varsayılan API anahtarı
API_KEY="zyYdg45BPnOjbVfeNn31OInPoiYii1pZ"

# Domaini kullanıcıdan al
read -p "Domaini girin (örnek: example.com): " DOMAIN_QUERY

# İlk script: Netlas sorgusu
COUNT=$(netlas count "domain:$DOMAIN_QUERY" --apikey "$API_KEY" --datatype domain --format json)
echo "COUNT output: $COUNT"

# Parse the JSON output to get the count
PARSED_COUNT=$(echo "$COUNT" | jq ".count")
echo "Parsed COUNT: $PARSED_COUNT"

# Check if COUNT is a valid integer and greater than 0
if [[ "$PARSED_COUNT" =~ ^[0-9]+$ ]] && [ "$PARSED_COUNT" -gt 0 ]; then
    netlas download "domain:$DOMAIN_QUERY" --apikey "$API_KEY" --datatype domain --include "domain" --count "$PARSED_COUNT" | jq -r ".data.domain"
else
    echo "No results for the given query."
fi

# İkinci script: Subdomainfinder scraping (browser olmadan)
python3 subdomainfinder.py "$DOMAIN_QUERY"
