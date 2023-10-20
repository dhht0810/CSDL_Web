package com.example.thu_vien.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.MapsId;
import lombok.Getter;
import lombok.Setter;

@Entity
@IdClass(com.example.thu_vien.model.xd_the_loaiId.class)
@Getter
@Setter
public class xd_the_loai {
    @Id
    private int id_truyen;

    @Id
    private int id_the_loai;

    @ManyToOne
    @MapsId("id_truyen")
    @JoinColumn(name = "id_truyen")
    private Truyen truyen;

    @ManyToOne
    @MapsId("id_the_loai")
    @JoinColumn(name = "id_the_loai")
    private The_loai the_loai;
}
