#!/usr/bin/awk -f

{
    for(i = 1; i <= length($0); i++)
        printf("%s ", substr($0, i, 1));
    print "";
}
