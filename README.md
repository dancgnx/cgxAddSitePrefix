[#](#) cgxAddSitePrefix

WARNING: USE AT YOUR OWN RISK

Add a list of prefix as global site prefixes

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Setup authentication as listed below
* Create a file with one prefix per line
* run the script using: python3 cgxAddSitePrefix.py -S <site name> -P <file with prefixes>

cgxAddSitePrefix.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)

Exmpale:
```
bash$ ./cgxAddSitePrefix.py -S "WASHINGTON DC" -P prefixes 
Added 2.3.4.0/24 to site
Added 20.30.0.0/16 to site
```
