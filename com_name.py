import whois
query = "https://jpn.nec.com"
result = whois.NICClient().whois_lookup({
    'whoishost': 'whois.jprs.jp'
  }, query + '/e', 0)
result = whois.parser.WhoisJp(query, result)
w = whois.whois(query)
