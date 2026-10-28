import dns.resolver

target_domain = "youtube.com"
records_type = ["A", "AAAA", "MX", "NS", "CNAME", "TXT", "SOA", "PTR", "SRV", "NAPTR"]

dns_resolver = dns.resolver.Resolver()

# for record_type in records_types:
#     try:
#         answer = dns_resolver.resolve(target_domain, record_type)
#         print(f"\n{record_type} Records for {target_domain}:")
#         for rdata in answer:
#             print(f"  {rdata.to_text()}")
#     except dns.resolver.NoAnswer:
#         print(f"\n{record_type} Records for {target_domain}: No answer")
#     except dns.resolver.NXDOMAIN:
#         print(f"\n{record_type} Records for {target_domain}: Domain does not exist")
#     except Exception as e:
#         print(f"\n{record_type} Records for {target_domain}: Error - {str(e)}")     

for record_type in records_type:
    try:
        answer = dns_resolver.resolve(target_domain, record_type)

    except dns.resolver.NoAnswer:
        continue  # Skip to the next record type if no answer is found

    print(f"\n{record_type} Records for {target_domain}:")
    for data in answer:
        print(f"{data}")
            # print(f" {data}")

    # for rdata in answer:
    #     print(f"  {rdata.to_text()}")
    # print(answer.response.to_text())  # Print the full DNS response for the record type
    # print(answer.response)

    # with open("dman.txt", "w") as file:
    #     for data in answer:
    #         file.write(data.to_text())
    #         file.write("\n")
        # file.write(answer.response.to_text())
        # file.write("\n=======================================\n")
        # file.write(answer.response)
