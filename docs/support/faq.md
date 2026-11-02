# Frequently asked questions

## What works without hardware?

`Hand.mock()` stores five software joint positions. The [first example](../getting-started/first-movement.md) shows commands and returned state. It does not simulate contact or prove device behavior.

## Can I switch the mock to a physical hand?

The current Linkerbot/OmniHand adapters reject unsupported operations before transport I/O. A working hardware integration is separate work; a constructor swap does not supply it. `Hand.stop()` is not an implemented physical emergency stop.

## Which environments have evidence?

Recorded local mock checks cover Python3.11 and3.12. The correction PR's hosted CI passed on Python3.11. This does not establish every declared Python/OS version, ROS distribution, Docker image, MoveIt setup or MuJoCo model.

## How many grasp entries are there?

Nine primary target sets plus three compatibility entries. `open` has empty targets and is not an alias for `relaxed_open`; see [grasp vocabulary](../concepts/grasp-taxonomy.md).

## Is live glove input, a data module or a dataset service available here?

Those capabilities are not supplied by the current Python interfaces. The [canned frame tutorial](../tutorials/03-teleoperation.md) reads no glove, and [training-data concepts](../concepts/training-data.md) announce no dataset, delivery date or compliance guarantee.

## Where can I ask a question?

Use [contact and reports](contact.md). No Discussions route, response SLA, hardware-conformity assurance or staffed support service is established by these Docs.
