package com.example.thu_vien.service;

import java.util.List;

import com.example.thu_vien.entities.Truyen;

public interface TruyenService {
    Iterable<Truyen> findAll();

    List<Truyen> search(String ten, String tacgia);

    Truyen findById(Integer id);

    void save(Truyen truyen);

    void delete(Integer id);
}
