#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>

struct word_prop
{
    char *str;
    int cnt;
};

int main()
{
    FILE *textfile;
    char *text;
    long numbytes;
    int32_t top_n = 5;

    textfile = fopen("words.txt", "r");
    if (textfile == NULL)
        return 1;

    // Get Length of the file using fssek and ftell
    fseek(textfile, 0L, SEEK_END);
    numbytes = ftell(textfile);
    fseek(textfile, 0L, SEEK_SET);

    // allocate memoery with length of the text we found
    text = (char *)calloc(numbytes, sizeof(char));
    if (text == NULL)
        return 1;
    // Read the context of the text file
    fread(text, sizeof(char), numbytes, textfile);
    fclose(textfile);
    char **frequentWords = find_frequent_words(*text, top_n);
    return 0;
}
char **find_frequent_words(const char *path, int32_t n)
{
    char *delimiter = " \n,.";
    char *token = strtok(path, delimiter);
    int *count = 0;
    printf(token);
    char **res = (char **)malloc(sizeof(char *) * n);

    return res;
}
int cmpstr(const void *a, const void *b)
{
    const char *pa = *(const char **)a;
    const char *pb = *(const char **)b;
    return strcmp(pa, pb);
}