# DNS Records
| Record Name | Function |
| - | - |
| A | This resolves domain name to IP, gives back IPv4. |
| AAAA | This is same as A record. Just resovles to IPv6. |
| CNAME | Canonical resolves domain to another domain. Basically gives aliases [ClickHereForExample](./cname.png)|
| MX | Mail Exchange. It tells which server to send email to for a particular domain. It genarally have 2 entries one primary and secondary|
| SOA | Stores administrative information about a DNS zone |
| NS | Provides the name of Authoritative Name server within a domain|
| SRV | It is a service record. Poins to a server and a service by including a port number [ClickHere](./srv.png)|
| PTR | It is oppostive of A or AAAA records. Resolves IP to domain names.They are attacked to email and used to stop email spam [Click](./ptr.png).|
| TXT | This Record contains miscellaneous info about a domain.|

A DNS database have a zone file. 
The zone file contains the DNS records.

CNAME records , resolved domain names to domain name.
>Cname | ftp.example.com | example.com | 7200

In this case it resolves ftp.example.com to example.com.