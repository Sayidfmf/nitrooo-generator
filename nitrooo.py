#!/bin/sh

# Colors
RED='\033[1;31m'
GRN='\033[0;32m'
NC='\033[0m'

clear
echo -e "${RED}Rewe Logs Generator - BY SOLRA${NC}"
echo ""

# Ask how many logs
echo -n "How many REWE logs to generate? > "
read AMOUNT
echo ""

# Start loop
i=1
while [ $i -le $AMOUNT ]; do
  RAND_ID=$((RANDOM % 1000))
  POINTS=$((1000 + RANDOM % 49001))

  case $((RANDOM % 10 + 1)) in
    1) FIRST="Jonas"; LAST="Becker";;
    2) FIRST="Nico"; LAST="Keller";;
    3) FIRST="Tom"; LAST="Meier";;
    4) FIRST="Lukas"; LAST="Neumann";;
    5) FIRST="Felix"; LAST="Brandt";;
    6) FIRST="Sophie"; LAST="Koch";;
    7) FIRST="Laura"; LAST="Richter";;
    8) FIRST="Anna"; LAST="Hofmann";;
    9) FIRST="Marie"; LAST="Lang";;
    10) FIRST="Lea"; LAST="Scholz";;
  esac

  DOMAIN=$( [ $((RANDOM % 2)) -eq 0 ] && echo "gmail.com" || echo "icloud.com" )
  EMAIL=$(echo "$FIRST.$LAST$RAND_ID@$DOMAIN" | tr '[:upper:]' '[:lower:]')

  case $((RANDOM % 4)) in
    0) PASSWORD="${FIRST}${RANDOM}%";;
    1) PASSWORD="${FIRST}${LAST}!$((RANDOM % 100))";;
    2) PASSWORD="${FIRST}2024!";;
    3) PASSWORD="Rewe$((RANDOM % 9999))";;
  esac

  if [ $((RANDOM % 2)) -eq 0 ]; then
    PREFIX="+49 157"
    NUMBER=$((1000000 + RANDOM % 8999999))
    PHONE="$PREFIX $NUMBER"
  else
    AREA=$((200 + RANDOM % 800))
    EXCHANGE=$((100 + RANDOM % 900))
    LINE=$((1000 + RANDOM % 9000))
    PHONE="+1 $AREA-$EXCHANGE-$LINE"
  fi

  echo -e "${RED}[$i] Name:${NC} $FIRST $LAST"
  echo -e "${RED}    Email:${NC} $EMAIL"
  echo -e "${RED}    Password:${NC} $PASSWORD"
  echo -e "${RED}    Phone:${NC} $PHONE"
  echo -e "${RED}    Payback Points:${NC} $POINTS"
  echo -e "${GRN}    [+] Account Status: VERIFIED${NC}"
  echo ""

  i=$((i+1))
done
