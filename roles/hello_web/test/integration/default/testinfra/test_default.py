#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_port_80_is_listening(host):
  socket = host.socket("tcp://80")
  assert(socket.is_listening)
