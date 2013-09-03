fakesleep
=========

fakesleep is a simple module for tests that use `time.sleep()`. Sleeping in
tests is generally considered bad (as it makes tests run slow). Using
sleep with `time.time()` can lead to spurious failures, as clock
precision / interpeter overhead can cause small differences in reported
times.

But sometimes, you need `sleep()`.

fakesleep provides a fake implementation of `time.sleep()` that doesn't
actually sleep. It also guarrantees "correct" results for calls to
`time.time()` and other time functions. Note that `datetime` functions are
**not** faked.

To install, simply call `fakesleep.monkey_patch()`. To restore the real versions, call `fakesleep.monkey_restore()`.

:author: Pete Fein <pete@wearpants.org>
:license: BSD
:versions: Python 2.7 & 3
:source: https://github.com/wearpants/fakesleep

