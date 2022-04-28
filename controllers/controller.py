from models.LinkedList import LinkedList


def inserir_inicio(linked_list, elemento):
    linked_list.insert_at_start(elemento)
    return linked_list

def inserir_final(linked_list, elemento):
    linked_list.insert_at_end(elemento)
    return linked_list

def inserir_depois_pais_registado(linked_list, elemento, registado):
    linked_list.insert_after_item(elemento, registado)
    return linked_list

def inserir_antes_pais_registado(linked_list,  elemento, registado):
    linked_list.insert_before_item(elemento, registado)
    return linked_list

def inserir_pais_determinado_indice(linked_list, elemento, valor):
    linked_list.insert_at_index(elemento, int(valor))
    return linked_list

def verificar_numero_elementos(linked_list):
    linked_list.get_count()
    return linked_list

def verificar_pais_lista(linked_list, elemento):
    if linked_list.search_item(elemento) == True:
        return True, linked_list
    else:
        return False

def eliminar_primeiro_elemento(linked_list):
    linked_list.delete_at_start()
    return linked_list


def eliminar_ultimo_elemento(linked_list):
    linked_list.delete_at_end()
    return linked_list


def eliminar_pais_selecionado(linked_list, elemento):
    linked_list.delete_element_by_value(elemento)
    return linked_list