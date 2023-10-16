package com.example.thu_vien.entities;

import java.util.HashSet;
import java.util.Set;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OrderBy;
import jakarta.persistence.OrderColumn;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name="truyen")
@Getter
@Setter
public class Truyen {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(insertable=false, updatable=false)
    private int id;
    private String ten;
    private String tacgia;
    private String tinh_trang;
    private int luot_thich;

    @OneToMany(mappedBy = "truyen", fetch = FetchType.LAZY)
    @OrderColumn(name = "idtr")
    @OrderBy("id_chap asc")
    private Set<Chap> chaps = new HashSet<>();

    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(name = "xd_the_loai", joinColumns = @JoinColumn(name = "id_truyen"), inverseJoinColumns = @JoinColumn(name = "id_the_loai"))
    @OrderBy("id asc")
    private Set<The_loai> the_loais = new HashSet<>();
}
