test.once:
	nosetests --with-yanc test/unit

test.continuously:
	bundle exec guard start --clear --notify=false
