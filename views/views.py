from models.LinkedList import LinkedList
from controllers import controller

def main ():
    linked_list = LinkedList()
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return
        

        if comandos [0] == "RPI":
            if controller.inserir_inicio(linked_list, comandos [1]):
                linked_list.traverse_list()

        if comandos[0] == "RPF":
            if controller.inserir_final(linked_list, comandos[1]):
                linked_list.traverse_list()


        if comandos[0] == "RPDE":
            if controller.inserir_depois_pais_registado(linked_list, comandos[2], comandos[1]):
                linked_list.traverse_list()


        if comandos[0] == "RPAE":
            if controller.inserir_antes_pais_registado(linked_list, comandos[2], comandos[1]):
                linked_list.traverse_list()
            

        if comandos[0] == "RPII":
            if controller.inserir_num_determinado_indice(linked_list, int(comandos[2]), comandos[1]):
                linked_list.traverse_list()


        if comandos[0] == "VNE":
            if controller.verificar_numero_elementos(linked_list):
                print(f"O número de elementos são {linked_list.get_count()}.")


        if comandos[0] == "VP":
            if controller.verificar_pais_lista(linked_list, comandos[1]):
                print(f"O país {comandos[1]} encontra-se na lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")


        if comandos[0] == "EPE":
            x = linked_list.start_node.item
            if controller.eliminar_primeiro_elemento(linked_list):
                print(f"O país {x} foi eliminado da lista.")


        if comandos[0] == "EUE":
            x = linked_list.get_last_node()
            if controller.eliminar_ultimo_elemento(linked_list):
                print(f"O país {x} foi eliminado da lista.")
        


        if comandos[0] == "EP":
            if controller.verificar_pais_lista(linked_list, comandos[1]):
                controller.eliminar_pais_selecionado(linked_list, comandos[1])
                print(f"O país {comandos[1]} foi eliminado da lista.")
            else:
                print(f"O país {comandos[1]} não se encontra na lista.")
        

        