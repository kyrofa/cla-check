import sys
from launchpadlib.launchpad import Launchpad


def run():
	if len(sys.argv) != 2:
		sys.exit('Expected a single argument of an email address')

	email = sys.argv[1]

	print('Logging into Launchpad...')
	launchpad = Launchpad.login_anonymously('check CLA', 'production')

	print('Checking for a Launchpad account associated with this email address...')
	contributor = launchpad.people.getByEmail(email=email)
	if not contributor:
		sys.exit('The contributor does not have a Launchpad account.')

	print('Contributor: {}'.format(contributor))

	print('Checking if the contributor has signed the CLA...')
	if contributor in launchpad.people['contributor-agreement-canonical'].participants:
		print('The contributor has signed the CLA.')
	else:
		sys.exit('The contributor has a Launchpad account, but has not signed the CLA.')
