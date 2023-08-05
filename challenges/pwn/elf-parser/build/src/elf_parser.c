#include <stdio.h>
#include <elf.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <string.h>

#define ELF_MAGIC 0x464c457f
#define MACH_MAGIC 0

typedef struct __attribute__((__aligned__(1))) {
    uint64_t address;
    uint64_t offset;
    char type[0x10];
    char name[0x15];
} Shdr;

void NnnNnnnnooOOoooOOOttTTTtttTTTbAAAaaaaaAAAaaaBbBbbbBAAAaAaaAdcccccCCCKkkkKKKkkkkkKKDdddDddddoOooOOooRrrrRrRrRr() {
    printf("Do you want a shell huh?\n");
    printf("no");
}

void init() {
    setbuf(stdin,  0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    alarm(0x30);
}

void elf_parse_exec(const char *buf) {

    struct {
        int shnum;
        uint64_t offset;
        Elf64_Shdr *sh_strtab;
        const char *sh_strtab_p;
        Elf64_Ehdr *ehdr;
        Elf64_Shdr *shdr;
        const char *t;
        int i;
        Shdr h;
    } frame;

    frame.ehdr = (Elf64_Ehdr *)buf;
    frame.shdr = (Elf64_Shdr *)(buf + frame.ehdr->e_shoff);
    frame.shnum = frame.ehdr->e_shnum;
    frame.offset = frame.ehdr->e_shoff;
    
    frame.sh_strtab = &(frame.shdr[frame.ehdr->e_shstrndx]);
    frame.sh_strtab_p = buf + frame.sh_strtab->sh_offset;
    printf("There are %d section headers, starting at offset 0x%lx:\n\n", frame.shnum, frame.offset);
    printf("Section Headers:\n");
    printf("  [Nr] %-20s %-16s %-16s %-8s\n", "Name", "Type", "Address", "Offset");
    
    for (frame.i = 0; frame.i < frame.shnum; ++frame.i) {
        frame.t = "NULL";
        switch(frame.shdr[frame.i].sh_type) {
        case 0:
        frame.t = "NULL"; break;
        case 1:
        frame.t = "PROGBITS"; break;
        case 2:
        frame.t = "SYMTAB"; break;
        case 3:
        frame.t = "STRTAB"; break;
        case 4:
        frame.t = "RELA"; break;
        case 5:
        frame.t = "HASH"; break;
        case 6:
        frame.t = "DYNAMIC"; break;
        case 7:
        frame.t = "NOTE"; break;
        case 8:
        frame.t = "NOBITS"; break;
        case 9:
        frame.t = "REL"; break;
        case 10:
        frame.t = "SHLIB"; break;
        case 11:
        frame.t = "DYNSYM"; break;
        case 12:
        frame.t = "NUM"; break;
        default:
        frame.t = "NULL"; break;
        }
        strcpy(frame.h.type, frame.t);
        strcpy(frame.h.name, frame.sh_strtab_p+frame.shdr[frame.i].sh_name);
        frame.h.address = frame.shdr[frame.i].sh_addr * 1;
        frame.h.offset = frame.shdr[frame.i].sh_offset * 1;
        printf("  [%2d] %-20s %-16s %016lx %08lx\n", frame.i, frame.h.name, frame.h.type, frame.h.address, frame.h.offset);
    }

}

void macho_parse_exec(const char *buf) {
    printf("err\n");
}

int main(int argc, const char **argv) {
    init();
    struct stat st = { 0 };
    if (argc != 3) {
        printf("Usage: parser -S filename\n");
        return 0;
    } 

    int fd = open(argv[2], O_RDONLY);
    if (fd < 0) {
        fprintf(stderr, "Failed to open file!\n");
        exit(1);
    }
    
    fstat(fd, &st);
    if (st.st_size <= 0) {
        fprintf(stderr, "Corrupted file!\n");
        exit(1);
    }

    const char *buf = mmap((void *)0x800000, st.st_size, PROT_EXEC | PROT_WRITE | PROT_READ, MAP_PRIVATE, fd, 0);
    if (!buf) {
        fprintf(stderr, "Failed to map file!\n");
        exit(1);
    }
    
    if (*(uint32_t *)buf == ELF_MAGIC) {
        // elf
        elf_parse_exec(buf);
    } else {
        fprintf(stderr, "Please input an ELF file!\n");
        exit(1);
    }
    return 0;
}
