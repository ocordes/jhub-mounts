#!/usr/bin/env python3

# created by: Oliver Cordes 2022-03-25
# changed by: Oliver Cordes 2022-03-25


from jhub_mounts.service import app, auth


app.run(port=4711, 
        debug=True)