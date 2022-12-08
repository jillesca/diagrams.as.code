from scour.scour import scourString as scour_string
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.iac import Ansible

diagram_att = {"pad": "0.2"}
docker_cluster_att = {"bgcolor": "#D8FCFF", "pencolor": "#17ECFF"}
cml_cluster_att = {"bgcolor": "#FFF7DE", "pencolor": "#FFD34D"}
edge_attr = {"style": "dashed"}

with Diagram("Using CML with Ansible on a Container", 
             show=False, 
             outformat="svg",  
             graph_attr=diagram_att
             ) as diagram:
    
    with Cluster("Docker", graph_attr=docker_cluster_att):
        ansible = Ansible("Ansible")
        
    with Cluster("Devnet Sandbox", graph_attr=cml_cluster_att):
        cml = Server("Cisco Modeling Labs")

    ansible - Edge(label="  API calls  ", **edge_attr) >> cml

full_filename = f"{diagram.filename}.{diagram.outformat}"
    
with open(full_filename, "rt") as file:
    generated_image = file.read()

with open(full_filename, "wt") as file:
    file.write(scour_string(generated_image))