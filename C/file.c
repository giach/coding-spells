#include<stdio.h>
#include<string.h>

int main() {

    FILE *fd;
    char s[30], scopy[30];
    char *token;
    int i;

    gets(s);

    // "r", "rw"
    fd = fopen("output.txt", "w+");

    fprintf(fd, "%s\n", s);

    for(i = 0; i < 30; i++) {
    	fprintf(fd, "%c ", s[i]);
    }
    fprintf(fd, "\n");

   strcpy(scopy, s);
   /* get the first token */
   token = strtok(scopy, " ");

   /* walk through other tokens */
   while( token != NULL ) {
      fprintf(fd, "%s ", token);

      token = strtok(NULL, " ");
   }
   fprintf(fd, "\n");


   	strcpy(scopy, s);
     /* get the first token */
   token = strtok(scopy, " ");

   /* walk through other tokens */
   while( token != NULL ) {
      fprintf(fd, "%s\n", token);

      token = strtok(NULL, " ");
   }
   fprintf(fd, "\n");
}
