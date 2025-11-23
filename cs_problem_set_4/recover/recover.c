#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Exactly one command-line argument allowed\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (!card)
    {
        printf("Cannot be opened for reading\n");
        return 1;
    }

    uint8_t buffer[512];
    int cnt = 0;
    FILE *image = NULL;

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (image)
            {
                fclose(image);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", cnt);
            image = fopen(filename, "w");
            cnt++;
        }

        if (image)
        {
            fwrite(buffer, 1, 512, image);
        }
    }
    if (image)
    {
        fclose(image);
    }
    fclose(card);
}
