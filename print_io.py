import pcbnew
import re

def print_sorted_pads_by_net(pcb_path):
    pcb = pcbnew.LoadBoard(pcb_path)

    for footprint in pcb.GetFootprints():
        if footprint.GetReference() == "U6":
            print(f"Component: {footprint.GetReference()} ({footprint.GetValue()})")
            
            pads_with_io_nets = []
            
            for pad in footprint.Pads():
                net = pad.GetNet()
                net_name = net.GetNetname() if net else None
                
                if net_name and net_name.startswith("/IO"):
                    pads_with_io_nets.append((pad.GetName(), net_name))
            
            pads_with_io_nets.sort(key=lambda x: x[1])
            sorted_pads = [pad[0] for pad in pads_with_io_nets]

            print("Array:", pads_with_io_nets)
            print("Size:", len(sorted_pads))
            print("Sorted Pads:", " ".join(sorted_pads))

if __name__ == "__main__":
    pcb_file = "ssla.kicad_pcb"
    
    print_sorted_pads_by_net(pcb_file)
