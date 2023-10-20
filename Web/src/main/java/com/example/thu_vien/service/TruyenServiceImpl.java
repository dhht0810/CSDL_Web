package com.example.thu_vien.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.thu_vien.dao.TruyenRepository;
import com.example.thu_vien.entities.Truyen;

@Service
public class TruyenServiceImpl implements TruyenService {
    @Autowired
    private TruyenRepository truyenRepository;

    @Override
    public Iterable<Truyen> findAll() {
        return truyenRepository.findAll();
    }

    @Override
    public List<Truyen> search(String ten, String tacgia) {
        return truyenRepository.findByTenContainingOrTacgiaContaining(ten, tacgia);
    }

    @Override
    public Truyen findById(Integer id) {
        return truyenRepository.findById(id).get();
    }

    @Override
    public void save(Truyen truyen) {
        truyenRepository.save(truyen);
    }

    @Override
    public void delete(Integer id) {
        truyenRepository.deleteById(id);
    }
}
