import argparse
parser = argparse.ArgumentParser()

#--pub_ssh_key_file ID_RSA.PUB pvt_ssh_key_file ID_RSA
parser.add_argument("-pubf","--pub_ssh_key_file", "---pub_ssh_key_file", help="Public key file name")
parser.add_argument("-pvtf","--pvt_ssh_key_file", "--pvt_ssh_key_file", help="Private key file name")


args = parser.parse_args()
print (args)


print( "Public key file name: {}\n Private key file name: {} ".format(
        args.pub_ssh_key_file,
        args.pvt_ssh_key_file,
        ))