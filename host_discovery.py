from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    dpid = event.dpid
    in_port = event.port
    src = packet.src
    dst = packet.dst

    # Learn MAC
    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][src] = in_port

    log.info("Host Detected: MAC=%s Switch=%s Port=%s", src, dpid, in_port)

    # If destination known → send directly
    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]

        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg)

    # Else flood
    else:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Host Discovery + Forwarding Started")