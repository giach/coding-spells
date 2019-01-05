#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct person {
    char name[30];
    int age;
    struct person *next;
};

struct person* add_elem(struct person *head, struct person *elem) {
    struct person *tmp;

    // daca nu exista niciun elemnt in lista, capatul de lista va
    // deveni chiar elementul ce trebuie adaugat
    if(head == NULL) {
        head = elem;
        return head;
    }

    tmp = head;
    // !!! tmp este un pointer auxiliar folosit pentru a ajunge la 
    // finalul listei unde se va insera noua structura 
    while(tmp->next != NULL) {
        tmp = tmp->next;
    }

    // am ajuns la finalul listei si putem adauga noul element
    tmp->next = elem;

    return head;
}


void print_list(struct person *head) {
    struct person *tmp;
    tmp = head;

   while(tmp != NULL) {
        printf("Nume = %s . Varsta = %d\n", tmp->name, tmp->age);
        tmp = tmp->next;
    }
}

void check_person(struct person *head, struct person *george) {

    struct person *tmp;
    // !!!! ATENTIE intotdeauna se foloseste un pointer auxiliar pentru a pargurge lista
    tmp = head;

    while(tmp != NULL) {
        // verifica daca elementul curent din lista este George
        if(strcmp(tmp->name, george->name) == 0 && tmp->age == george->age) {
            // George a fost fasit in lista si se verifica daca urmatoarea persoana e mai mare
            if(tmp->next != NULL && george->age < tmp->next->age ) {
                printf("urmatoarea persoana este mai mare decat George\n");
                return;
            }
            else {
                printf("urmatoarea persoana nu este mai mare decat George sau nu exista\n");
                return;
            }
        }

        tmp = tmp->next;
    }
    printf("George nu a fost gasit in lista\n");
}


int main() {

    struct person *list = NULL;
    struct person *g, *h, *y;
    
    // aloca memorie pentru prima persoana si populeaza structura
    g = (struct person*)malloc(sizeof(struct person));
    scanf("%s", g->name);
    scanf("%d", &g->age);
    g->next = NULL;

    // aloca memorie pentru a doua persoana si populeaza structura
    h = (struct person*)malloc(sizeof(struct person));
    scanf("%s", h->name);
    scanf("%d", &h->age);
    h->next = NULL;

    // aloca memorie pentru a treia persoana si populeaza structura
    y = (struct person*)malloc(sizeof(struct person));
    scanf("%s", y->name);
    scanf("%d", &y->age);
    y->next = NULL;



    // adauga prima persoana in lista
    list = add_elem(list, g);

    // adauga a doua persoana in lista
    list = add_elem(list, h);

    // adauga a treia persoana in lista
    list = add_elem(list, y);

    // afiseaza toate persoanele din lista
    print_list(list);

    // verifica daca prima g este in lista si daca este mai mic decat urmatoarea persoana din lista
    check_person(list, g);
    return 0;
    
}
