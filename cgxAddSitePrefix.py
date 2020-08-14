#!/usr/bin/env python3
import cgxinit
import cloudgenix
import sys


# create CGX object and authenticate

if __name__ == "__main__":
    cgx, args = cgxinit.go()

    # create a list of IP addresses
    ip_list = [
        line.strip() for line in args['prefixes_file'].readlines()
    ]

    # find site
    for site in cgx.get.sites().cgx_content['items']:
        if site['name'] == args['site_name']:
            site_id = site['id']
            break
    else:
        print("ERROR: Site not found")
        sys.exit()

    # get exiting list of prefixes
    existing = [
        lan['ipv4_config']["prefixes"][0]
        for lan in cgx.get.lannetworks(site_id).cgx_content['items']
    ]

    template = {"name":"REPLACE", "description":None,"tags":None,"ipv4_config":{"prefixes":["REPLACE"],"dhcp_relay":None,"dhcp_server":None,"default_routers":None},"scope":"global","network_context_id":None}

    # add one prefix at a time
    for prefix in ip_list:
        if prefix in existing:
            print(f"{prefix} already exists")
        else:
            # add prefix to cgx
            template['ipv4_config']['prefixes'] = [prefix]
            template['name'] = "p-" + prefix

            res = cgx.post.lannetworks(site_id, template)
            if not res:
                print(f"ERROR: Couldn't add {prefix}")
                cloudgenix.jd_detailed(res)
                sys.exit()
            else:
                print(f"Added {prefix} to site")


