
package com.example.thu_vien.controller;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.example.thu_vien.dao.ChapRepository;
import com.example.thu_vien.dao.The_loaiRepository;
import com.example.thu_vien.dao.sapxep;
import com.example.thu_vien.dao.DAO;
import com.example.thu_vien.entities.Chap;
import com.example.thu_vien.entities.The_loai;
import com.example.thu_vien.entities.Truyen;
import com.example.thu_vien.service.ChapService;
import com.example.thu_vien.service.TruyenService;

import jakarta.validation.Valid;

@Controller
public class mainController {
    @Autowired
    private TruyenService truyenService;
    @Autowired
    private sapxep l;
    @Autowired
    private DAO dao;
    @Autowired
    private The_loaiRepository the_loaiRepository;
    @Autowired
    private ChapService chapService;

    @GetMapping(value = {"/search"})
    public String search(Model model,@RequestParam("ten") String ten) {
        if (ten == "") {
            return "redirect:/";
        }
        model.addAttribute("listTruyen", truyenService.search(ten, ten));
        return "tim_kiem";
    }

    @GetMapping("/sapxep/{name}")
    public String sort(Model model, @PathVariable String name) {
        model.addAttribute("sap_xep", l.sap_xep(name));
        return "sapxep";
    }

    @GetMapping(value = {"/","/home"})
    public String show(Model model) {
        model.addAttribute("theloai", the_loaiRepository.findAll());
        return "home";
    }

    @GetMapping("/theloai/{id}")
    public String the_loai(Model model,@PathVariable int id) {
        model.addAttribute("tim_the_loai", dao.find(id));
        return "theloai";
    }

    @GetMapping("/truyen/{id}")
    public String truyen(Model model,@PathVariable int id) {
        model.addAttribute("truyen", truyenService.findById(id));
        return "truyen";
    }

    @GetMapping("/truyen/{id}/chap{c}")
    public String chap(Model model, @PathVariable int id, @PathVariable int c) {
        List<Chap> list = new ArrayList<Chap>();
        list.addAll(truyenService.findById(id).getChaps());
        if(c>1) {
            model.addAttribute("chaptruoc", list.get(c-1));
        } else {
            model.addAttribute("chaptruoc", list.get(c));
        } 
        model.addAttribute("chaphientai", list.get(c));
        if(c < list.size() - 1) {
            model.addAttribute("chapsau", list.get(c+1));
        } else {
             model.addAttribute("chapsau", list.get(c));
        }
        model.addAttribute("danhsachchap", truyenService.findById(id).getChaps());
        model.addAttribute("truyen", truyenService.findById(id));
        return "chap";
    }

    @GetMapping("/admin")
    public String admin(Model model) {
        model.addAttribute("truyen", truyenService.findAll());
        return "admin";
    }

    @GetMapping("/admin/update/truyen/{id}")
    public ModelAndView edit(@PathVariable(name = "id") Integer id) {
        Truyen truyen = truyenService.findById(id);
        ModelAndView mav = new ModelAndView("form");
        mav.addObject("truyen", truyen);
        List<The_loai> the_loais = (List<The_loai>) the_loaiRepository.findAll();
        mav.addObject("theloai", the_loais);
        mav.addObject("listchap", truyen.getChaps().size()-1);
        mav.addObject("chapmoi", new Chap(id));
        return mav;
    }

    @GetMapping("/admin/add")
    public ModelAndView add() {
        Truyen truyen = new Truyen();
        ModelAndView mav = new ModelAndView("form");
        mav.addObject("truyen", truyen);
         
        List<The_loai> the_loais = (List<The_loai>) the_loaiRepository.findAll();
         
        mav.addObject("theloai", the_loais);
         
        return mav;    
    }

    @PostMapping("/admin/save")
    public String save(@Valid Truyen truyen, @Valid Chap chap, BindingResult result) {
        if(result.hasErrors()) {
            return "form";
        }
        chapService.save(chap);
        truyenService.save(truyen);
        return "redirect:/admin";
    }

    @GetMapping("/test/{id}")
    public String test(Model model,@PathVariable int id) {
        model.addAttribute("test", dao.showChaps(id));
        return "test";
    }
}
