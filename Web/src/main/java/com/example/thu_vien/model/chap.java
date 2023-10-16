package com.example.thu_vien.model;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class chap {
    private int id;
    private int id_truyen;
    private String filePath;
    private int id_chap;

    public chap(int id_chap, String filePath) {
        this.id_chap = id_chap;
        this.filePath = filePath;
    }

    public chap(int id, int id_truyen, String filePath, int id_chap) {
        this.id = id;
        this.id_truyen = id_truyen;
        this.filePath = filePath;
        this.id_chap = id_chap;
    }
}
