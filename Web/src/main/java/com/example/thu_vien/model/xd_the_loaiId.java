package com.example.thu_vien.model;

import java.io.Serializable;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class xd_the_loaiId implements Serializable{
    private int id_truyen;
    private int id_the_loai;

    public xd_the_loaiId(int id_truyen, int id_the_loai) {
        this.id_truyen = id_truyen;
        this.id_the_loai = id_the_loai;
    }
}
