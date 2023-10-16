package com.example.thu_vien.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class truyen {
    private int id;
    private String ten;
    private String tacgia;
    private String anh;

    public truyen(int id, String truyen, String tac_gia, String anh) {
        this.id = id;
        this.ten = truyen;
        this.tacgia = tac_gia;
        this.anh = anh;
    }
}
