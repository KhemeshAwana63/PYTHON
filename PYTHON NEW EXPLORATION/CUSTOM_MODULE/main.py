"""as you can see i have imported all the modules both directly
and from package"""

import module as m1
m1.hello()

from packages.module2 import greetings
greetings()


from packages import module3
module3.welcome()

