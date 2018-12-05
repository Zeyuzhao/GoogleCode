#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: LED

short_description: Raspberry Pi LED Module

version_added: "2.4"

description:
    - "A module for interfacing with the raspberry pi GPIO, turning on/off GPIO"

options:
    pin:
        description:
            - Set the target pin
        required: true
    value:
        description:
            - Change value of pin
        required: true

author:
    - Zach Zhao (@thezachzhao)
'''

EXAMPLES = '''
# Set Pin 1 to High
- name: Turn on pin 1
  LED:
    name: hello world
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        pin=dict(type='int', required=True),
        value=dict(type='bool', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    # result = dict(
    #     changed=False,
    #     original_message='',
    #     message=''
    # )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    p = module.params["pin"]
    v = module.params["value"]
    
    try:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH if v else GPIO.LOW)
    except Exception as e:
        module.fail_json(msg='GPIO {0} failed: '.format(p) + str(e))

    results = {}
    module.exit_json(**results)

def main():
    run_module()

if __name__ == '__main__':
    main()